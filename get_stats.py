def find_potential_rating(text,overall_rating):
    p_rating = text.find('section', attrs = {'class':'card spacing'}).find_all('span')
    for element in p_rating:
        if element.string == overall_rating:
            continue
        elif int(element.string) < int(overall_rating):
            continue
        else:
            return element.string
            