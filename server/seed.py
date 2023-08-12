import random
from app import app
from models import Swimmer, Team, Event, Time, db

def create_swimmers(teams):
    names = [
        "John Smith", "Jane Johnson", "Michael Brown", "Emily Jones",
        "William Miller", "Olivia Davis", "James Garcia", "Emma Wilson",
        "Robert Martinez", "David Anderson", "Sophia Williams", "Mia Garcia",
        "Elijah Robinson", "Ava Lee", "Oliver Scott", "Isabella Evans",
        "Sophia Hernandez", "Logan Murphy", "Harper Turner", "Ethan Parker",
        "Amelia Moore", "Aiden Richardson", "Mia Hall", "Benjamin Reed",
        "Evelyn Coleman", "Lucas Perry", "Abigail Sanders", "Alexander Bennett",
        "Charlotte Simmons", "Michael Richardson", "Grace Butler",
        "Daniel Thompson", "Scarlett Mitchell", "Henry Hayes", "Elizabeth Simmons",
        "David White", "Chloe Lewis", "Joseph Martin", "Madison Simmons",
        "Noah Walker", "Emily Sanders", "Daniel Rogers", "Zoe Hill",
        "Ella Bennett", "Carter Murphy", "Grace Torres", "Lucas Howard"
    ]

    for team in teams:
        
        team_swimmers = random.sample(names, 10)
        for swimmer_name in team_swimmers:
            swimmer = Swimmer(name=swimmer_name, team=team)
            db.session.add(swimmer)  
            db.session.commit()

def create_times():
    all_swimmers = Swimmer.query.all()
    all_events = Event.query.all()

    for swimmer in all_swimmers:
        for event in all_events:
            time = round(random.uniform(50.0, 300.0), 2)
            time_entry = Time(swimmer=swimmer, event=event, time=time)
            db.session.add(time_entry) 
            db.session.commit()
            
if __name__ == "__main__":
    with app.app_context():
        print("Clearing db...")
        Swimmer.query.delete()
        Team.query.delete()
        Event.query.delete()
        Time.query.delete()

        print("Seeding teams...")
        teams = [Team(name=team_name) for team_name in [
            "Barclay Farms", "Charleston", "Cherry Valley", "Covered Bridge",
            "Downs Farm", "Erlton", "Fox Hollow", "Haddowntowne", "Old Orchard",
            "Wexford Leas", "Willowdale", "Woodcrest"
        ]]
        db.session.add_all(teams)
        db.session.commit()

        print("Seeding swimmers...")
        create_swimmers(teams)

        print("Seeding events...")
        events = [Event(name=event_name) for event_name in [
            "200 Medley Relay", "200 Freestyle", "200 IM", "50 Freestyle",
            "100 Butterfly", "100 Freestyle", "500 Freestyle", "200 Free Relay",
            "100 Backstroke", "100 Breaststroke", "400 Free Relay"
        ]]
        db.session.add_all(events)
        db.session.commit()

        print("Seeding times...")
        create_times()
        
        print("Done seeding!")
