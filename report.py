def main():
    spacecraft = {'name':'Crew Dragon', 'crew':'4', 'fuel':'1000'}
    spacecraft.update({'distance':0.01, 'orbit':'Sun'})
    print(creat_report(spacecraft))


def creat_report(spacecraft):
    return f'''
    ============== REPORT ==============

    Name: {spacecraft.get('name','Unknown')}
    Crew: {spacecraft.get('crew','Unknown')}
    Fuel: {spacecraft.get('fuel','Unknown')}
    Distance: {spacecraft.get('distance','Unknown')} AU
    Orbit: {spacecraft.get('orbit','Unknown')}
    
    ====================================    
'''
main()
