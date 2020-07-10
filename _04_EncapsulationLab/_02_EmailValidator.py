class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = int(min_length)
        self.mails = list(mails)
        self.domains = list(domains)

    def __validate_name(self, name):
        v_name = len(name) >= self.min_length
        return v_name

    def __validate_mail(self, mail):
        v_mail = mail in self.mails
        return v_mail

    def __validate_domain(self, domain):
        v_domain = domain in self.domains
        return v_domain

    def validate(self, email):
        name = email[:email.index('@')]
        mail = email[email.index('@') + 1: email.index('.')]
        domain = email[email.index('.') + 1:]
        v_name = self.__validate_name(name)
        v_mail = self.__validate_mail(mail)
        v_domain = self.__validate_domain(domain)
        return v_name and v_mail and v_domain


mails = ["gmail", "softuni"]
domains = ["com", "bg", "co.uk"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
