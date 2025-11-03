import re
from collections import Counter

def parse_accepted_logins(lines):
    pattern = r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}).*Accepted.*from\s+([0-9.]+)'
    logins = []
    for line in lines:
        match = re.search(pattern, line)
        if match:
            logins.append({
                'timestamp': match.group(1),
                'ip': match.group(2)
            })
    return logins

def summarize_logins(logins):
    ip_count = Counter(login['ip'] for login in logins)
    summary = [{'ip': ip, 'count': count} for ip, count in ip_count.items()]
    return sorted(summary, key=lambda x: x['count'], reverse=True)
