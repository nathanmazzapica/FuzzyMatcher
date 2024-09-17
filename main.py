from time import perf_counter
import verbose_logger
from verbose_logger import create_logger, clear_log, print_log, view_log

STDOUT = create_logger("stdout")
MAX_LEN_DIFF = 4

# Reconsider using default arg for log, I'd prefer to keep algorithm functions and logger decoupled
# TODO: Implement proper insertion method, if one letter is missing, we should only need to make one change
def compare_strings(s1, s2, log=STDOUT):
    changes = 0
    checking_string = s1
    s1 = s1.lower()
    s2 = s2.lower()

    log(f"Testing {s1} against {s2}")

#    if len(s2) > len(s1):
#        temp = s1
#        s1 = s2
#        s2 = temp

    for i in range(len(s1)):
        char_to_check = s1[i]

        try:
            compared_to = s2[i]
        except IndexError:
            new_changes = (len(s1) - len(s2))
            log(f"Reached the end of {s2}, adding {new_changes} new changes.")
            changes += new_changes
            break

        if char_to_check == compared_to:
            continue

        log(f"{compared_to} is not {char_to_check}, adding one change")
        changes += 1

    return changes

def get_most_similar(entry, known):
    known_copy = known.copy()
    filtered = list(filter(lambda s: abs(len(s) - len(entry)) < MAX_LEN_DIFF, known_copy))
    STDOUT(f"Filtered countries from {len(known)} entries to {len(filtered)} entries\n{filtered}")
    most_similar = ("ok", 999)
    for string in filtered:
        log = create_logger(string)
        changes = compare_strings(string, entry, log)

        if changes < most_similar[1]:
            STDOUT(f"Changing most_similar from {most_similar} to {(string, changes)}.")
            most_similar = (string, changes)

        log(f"Result: {(string, changes)}")
    return most_similar[0]





def main():
    countries = [
        "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia",
        "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium",
        "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria",
        "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic",
        "Chad", "Chile", "China", "Colombia", "Comoros", "Congo (Congo-Brazzaville)", "Costa Rica", "Croatia",
        "Cuba", "Cyprus", "Czechia (Czech Republic)", "Democratic Republic of the Congo", "Denmark", "Djibouti",
        "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea",
        "Estonia", "Eswatini (fmr. Swaziland)", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia",
        "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras",
        "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan",
        "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho",
        "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives",
        "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco",
        "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (formerly Burma)", "Namibia", "Nauru", "Nepal",
        "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia", "Norway",
        "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland",
        "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia",
        "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal",
        "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia",
        "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden",
        "Switzerland",
        "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago",
        "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom",
        "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam",
        "Yemen", "Zambia", "Zimbabwe", "Wales", "US Virgin Islands", "Korea"
    ]

    test_cases = [
        ("slavania", "Slovenia"),
        ("Inia", "India"),
        ("pamama", "Panama"),
        ("wails", "Wales"),
        ("koria", "Korea"),
        ("untied states", "United States of America"),
        ("brazi", "Brazil"),
        ("argentin", "Argentina"),
        ("gemany", "Germany"),
        ("afghanstan", "Afghanistan"),
        ("japon", "Japan"),
        ("austrila", "Australia"),
        ("candada", "Canada"),
        ("spaen", "Spain"),
        ("italy", "Italy"),
        ("portgual", "Portugal"),
        ("mexcio", "Mexico"),
        ("new zeland", "New Zealand"),
        ("frace", "France"),
        ("nigerai", "Nigeria"),
        ("ethophia", "Ethiopia"),
        ("greecee", "Greece"),
        ("nroway", "Norway"),
        ("finand", "Finland"),
        ("south korera", "South Korea"),
        ("north korera", "North Korea"),
        ("vietman", "Vietnam"),
        ("chille", "Chile"),
        ("colmbia", "Colombia"),
        ("indnesia", "Indonesia"),
        ("serba", "Serbia"),
        ("saudi arabia", "Saudi Arabia")
    ]

    case_number = 1
    for case in test_cases:
        trying = case[0]
        start = perf_counter()
        output = get_most_similar(trying, countries)
        end = perf_counter()
        time_to_execute = (end - start) * 1000
        STDOUT(f"Time to execute: {time_to_execute}ms")
        print(f"\n=========CASE {case_number}============")
        print(f"Input: {trying}\nExpecting: {case[1]}\nActual: {output}")
        print(f"=========CASE {case_number}============\n")

        next_instr = ""


        while next_instr != "n":

            if next_instr == "vr":
                cases = [case[1], output]
                view_log(cases)

            if next_instr == "s":
                view_log(["stdout"])
                input()

            if next_instr != '' and next_instr[0].lower() == 'v':
                cases = next_instr[2::].split(';')
                print(cases)
                view_log(cases)
                print(
                    f"Changes to {output}: {compare_strings(trying, output)}\nChanges to expected: {compare_strings(case[1], trying)}")
                input()

            next_instr = input(
                "Enter 'vr' to view relevant logs\nEnter 'v' to view specific logs by country\nEnter 's' to view stdout\nEnter 'n' to continue to next case...")



        verbose_logger.clear_log()
        case_number += 1





if __name__ == '__main__':
    main()