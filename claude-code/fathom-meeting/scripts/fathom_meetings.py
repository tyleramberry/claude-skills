#!/usr/bin/env python3
"""
Fetch meeting notes (summary + action items) from the Fathom API.

Loads FATHOM_API_KEY from an .env file (never prints the value), queries
GET https://api.fathom.ai/external/v1/meetings with the given filters, and
writes the raw JSON response to --out (or stdout). Always requests
include_summary and include_action_items — that's all this skill needs.

Usage:
  python3 fathom_meetings.py --after 2026-09-02T00:00:00Z --before 2026-09-05T00:00:00Z \
      --out /tmp/meetings.json

Handles pagination transparently: if the response has a next_cursor, keeps
fetching and merges all `items` into one list before writing out.
"""
import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

DEFAULT_ENV_PATH = os.path.expanduser("~/second-brain/.env")
API_BASE = "https://api.fathom.ai/external/v1/meetings"


def load_api_key(env_path):
    if os.environ.get("FATHOM_API_KEY"):
        return os.environ["FATHOM_API_KEY"]
    if not os.path.isfile(env_path):
        return None
    with open(env_path) as f:
        for line in f:
            m = re.match(r'^\s*FATHOM_API_KEY\s*=\s*(.+?)\s*$', line)
            if m:
                return m.group(1).strip().strip('"').strip("'")
    return None


def fetch_all(api_key, params):
    items = []
    cursor = None
    while True:
        q = dict(params)
        if cursor:
            q["cursor"] = cursor
        url = API_BASE + "?" + urllib.parse.urlencode(q, doseq=True)
        req = urllib.request.Request(url, headers={"X-Api-Key": api_key})
        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            body = e.read().decode(errors="replace")
            print(f"HTTP {e.code} from Fathom API: {body}", file=sys.stderr)
            sys.exit(1)
        items.extend(data.get("items", []))
        cursor = data.get("next_cursor")
        if not cursor:
            break
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--after", required=True, help="created_after, ISO 8601 e.g. 2026-09-02T00:00:00Z")
    ap.add_argument("--before", required=True, help="created_before, ISO 8601")
    ap.add_argument("--recorded-by", action="append", default=[], help="filter: recorded_by[] email (repeatable)")
    ap.add_argument("--teams", action="append", default=[], help="filter: teams[] name (repeatable)")
    ap.add_argument("--env-path", default=DEFAULT_ENV_PATH, help="path to .env containing FATHOM_API_KEY")
    ap.add_argument("--out", help="write JSON here instead of stdout")
    args = ap.parse_args()

    api_key = load_api_key(args.env_path)
    if not api_key:
        print(
            f"No FATHOM_API_KEY found (checked $FATHOM_API_KEY and {args.env_path}). "
            "Point --env-path at the .env file that holds your Fathom API key.",
            file=sys.stderr,
        )
        sys.exit(1)

    params = {
        "created_after": args.after,
        "created_before": args.before,
        "include_summary": "true",
        "include_action_items": "true",
    }
    if args.recorded_by:
        params["recorded_by[]"] = args.recorded_by
    if args.teams:
        params["teams[]"] = args.teams

    items = fetch_all(api_key, params)
    out = json.dumps({"items": items}, indent=2)

    if args.out:
        with open(args.out, "w") as f:
            f.write(out)
        print(f"Wrote {len(items)} meeting(s) to {args.out}")
    else:
        print(out)


if __name__ == "__main__":
    main()
