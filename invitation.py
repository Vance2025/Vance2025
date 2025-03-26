def main():
    guest_list = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for name in guest_list:
        print(write_letter(name, "Princess Peach"))


def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+

        Dear {receiver},
        
        You are cordially invited to
        a ball at Princess Peach's
        castle this evening 7:00PM.

        Sincerely,
        {sender}

    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """

print(write_letter('Vance', 'Princess'))

main()
