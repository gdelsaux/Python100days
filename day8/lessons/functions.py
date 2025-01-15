def points_in_word(combined_name, word_to_iterate):
    score = 0
    for letter in range(len(combined_name)):
        if combined_name[letter] in word_to_iterate:
            score += 1
    return score
    
def calculate_love_score(name1, name2):
    combined_name = (name1 + name2).lower()
    true_score = str(points_in_word(combined_name, "true"))
    love_score = str(points_in_word(combined_name, "love"))

    print(true_score + love_score)

calculate_love_score("Kanye West", "Kim Kardashian")