#!/usr/bin/env sh
set -e

if ! command -v curl >/dev/null 2>&1; then
    apk add --no-cache curl >/dev/null
fi

/app/update_cloudflare_ips.sh || true

(
    while true; do
        sleep 12h
        /app/update_cloudflare_ips.sh || true
    done
) &
