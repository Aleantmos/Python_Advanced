class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def is_name_valid(self, name):
        return len(name) >= self.min_length

    def is_mail_valid(self, mail):
        return mail in self.mails

    def is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        parts = email.split('@')
        if len(parts) != 2:
            return False

        username, rest = parts
        mail_domain_parts = rest.split('.')

        if len(mail_domain_parts) < 2:
            return False

        mail = mail_domain_parts[0]
        domain = ".".join(mail_domain_parts[1:])

        return (self.is_name_valid(username) and
                self.is_mail_valid(mail) and
                self.is_domain_valid(domain))