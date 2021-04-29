class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # rules:
        # '.' in local part of email can be ignored.
        # eveything after '+' in local part can be ignored.
        # local rules can happen together.
        # '.' in domain cannot be ignored.
        
        return_emails = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local, ignore = email.split('+', 1)
            local = local.replace('.','')
            return_emails.add(local+'@'+domain)
        return len(return_emails)