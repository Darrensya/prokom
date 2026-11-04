favorite_languages = {   
                    'jen': 'python',    
                    'sarah': 'c',    
                    'edward': 'rust',    
                    'phil': 'python',      
}

orang =['jen', 'ren', 'phil', 'keii', 'sarah']

for seorang in orang :
    if seorang in favorite_languages:
        print(f"Terimakasih sudah voting {seorang.title()}!")
    else :
        print(f"Tolong bantu kita voting, {seorang.title()}")
        