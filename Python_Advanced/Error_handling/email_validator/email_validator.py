from Error_handling.email_validator.custom_exceptions \
    import MustContainAtSymbolError, NameTooShortError, InvalidDomainError

line = input()

while line != "End":
    email = line
    email_parts = email.split("@")

    if len(email_parts) != 2:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain_part = email_parts

    if len(name) < 5:
        raise NameTooShortError("Name must be more than 4 characters")

    domains = [".com", ".bg", ".org", ".net"]
    domain = f".{domain_part.split('.')[-1]}"

    if domain not in domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid!")
    line = input()