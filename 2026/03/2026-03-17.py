def get_milestone(years):
    match years:
        case years if years == 0:
            return "Newlyweds"
        case years if 0 < years < 5:
            return "Paper"
        case years if 5 <= years < 10:
            return "Wood"
        case years if 10 <= years < 25:
            return "Tin"
        case years if 25 <= years < 40:
            return "Silver"
        case years if 40 <= years < 50:
            return "Ruby"
        case years if 50 <= years < 60:
            return "Gold"
        case years if 60 <= years < 70:
            return "Diamond"
        case years if 70 <= years:
            return "Platinum"


assert get_milestone(0) == "Newlyweds"
assert get_milestone(1) == "Paper"
assert get_milestone(8) == "Wood"
assert get_milestone(10) == "Tin"
assert get_milestone(26) == "Silver"
assert get_milestone(45) == "Ruby"
assert get_milestone(50) == "Gold"
assert get_milestone(64) == "Diamond"
assert get_milestone(71) == "Platinum"
