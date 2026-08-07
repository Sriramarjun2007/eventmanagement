from django.shortcuts import render


EVENTS = {

    1: {
        "title": "Tech Conference 2024",
        "type": "Corporate Event",
        "budget": "100000-200000",
        "location": "Chennai",
        "venue_type": "Convention Center",
        "image": "images/event1.jpg",

        "short_description":
            "A premier tech conference showcasing the latest innovations and trends in the industry.",

        "description":
            "Join us for the Tech Conference 2024, a leading event for technology professionals, innovators, and enthusiasts. This conference will feature keynote speeches from industry leaders, interactive workshops, networking opportunities, AI, cybersecurity and cloud computing sessions.",

        "services": [
            "Keynote Speakers",
            "Interactive Workshops",
            "Networking Events",
            "Exhibition Hall",
        ],

        "attendees": "500+ Attendees",
        "speakers": "30+ Speakers",
        "duration": "2-Day Event",
        "venue": "Downtown Convention Center",
    },


    2: {
        "title": "Corporate Events",
        "type": "Corporate Event",
        "budget": "200000-500000",
        "location": "Bangalore",
        "venue_type": "Banquet Hall",
        "image": "images/event2.jpg",

        "short_description":
            "Professional and impactful corporate gatherings.",

        "description":
            "Create a professional and memorable corporate event with our complete event management services.",

        "services": [
            "Corporate Planning",
            "Professional Catering",
            "Guest Management",
            "Audio Visual Setup",
        ],

        "attendees": "300+ Attendees",
        "speakers": "20+ Speakers",
        "duration": "1-Day Event",
        "venue": "Business Convention Center",
    },


    3: {
        "title": "Private Parties",
        "type": "Birthday party",
        "budget": "50000-100000",
        "location": "Coimbatore",
        "venue_type": "Hotel",
        "image": "images/event3.jpg",

        "short_description":
            "Memorable and fun private parties.",

        "description":
            "Celebrate your special moments with a beautifully planned private party.",

        "services": [
            "Theme Decoration",
            "Entertainment",
            "Food & Catering",
            "Guest Management",
        ],

        "attendees": "150+ Guests",
        "speakers": "10+ Performers",
        "duration": "1-Day Event",
        "venue": "Private Celebration Hall",
    },


    4: {
        "title": "Festivals",
        "type": "Corporate Event",
        "budget": "Above-500000",
        "location": "Chennai",
        "venue_type": "Outdoor / Open Ground",
        "image": "images/event4.jpg",

        "short_description":
            "Large-scale music and arts festivals.",

        "description":
            "Experience professionally managed festivals designed to bring communities together.",

        "services": [
            "Stage Management",
            "Artist Management",
            "Vendor Management",
            "Security Coordination",
        ],

        "attendees": "1000+ Attendees",
        "speakers": "50+ Artists",
        "duration": "3-Day Event",
        "venue": "City Festival Grounds",
    },


    5: {
        "title": "Weddings",
        "type": "Wedding",
        "budget": "200000-500000",
        "location": "Chennai",
        "venue_type": "Banquet Hall",
        "image": "images/event5.jpg",

        "short_description":
            "Elegant and personalized wedding celebrations.",

        "description":
            "Make your wedding day unforgettable with elegant planning and personalized experiences.",

        "services": [
            "Wedding Decoration",
            "Catering",
            "Photography",
            "Guest Management",
        ],

        "attendees": "500+ Guests",
        "speakers": "10+ Professionals",
        "duration": "2-Day Event",
        "venue": "Grand Wedding Hall",
    },


    6: {
        "title": "Summer Music Festival",
        "type": "Engagement",
        "budget": "100000-200000",
        "location": "Bangalore",
        "venue_type": "Outdoor / Open Ground",
        "image": "images/event6.jpg",

        "short_description":
            "An outdoor celebration of music and community.",

        "description":
            "Enjoy a vibrant outdoor music festival featuring talented performers, food vendors and entertainment.",

        "services": [
            "Live Music",
            "Stage Management",
            "Food Vendors",
            "Security",
        ],

        "attendees": "2000+ Attendees",
        "speakers": "50+ Artists",
        "duration": "3-Day Event",
        "venue": "Outdoor Festival Ground",
    },


    7: {
        "title": "Corporate Gala Night",
        "type": "Corporate Event",
        "budget": "200000-500000",
        "location": "Coimbatore",
        "venue_type": "Convention Center",
        "image": "images/event7.jpg",

        "short_description":
            "An elegant evening for networking and recognition.",

        "description":
            "Host an elegant corporate gala designed for networking, employee recognition, awards and professional celebrations.",

        "services": [
            "Awards Ceremony",
            "Professional Catering",
            "Stage Design",
            "Guest Management",
        ],

        "attendees": "400+ Attendees",
        "speakers": "25+ Speakers",
        "duration": "1-Day Event",
        "venue": "Grand Convention Hall",
    },


    8: {
        "title": "Art Exhibition Opening",
        "type": "Corporate Event",
        "budget": "50000-100000",
        "location": "Madurai",
        "venue_type": "Hotel",
        "image": "images/event8.jpg",

        "short_description":
            "Showcasing contemporary art from emerging artists.",

        "description":
            "A professionally managed art exhibition featuring contemporary artists and creative professionals.",

        "services": [
            "Exhibition Setup",
            "Artist Management",
            "Guest Registration",
            "Media Coordination",
        ],

        "attendees": "300+ Guests",
        "speakers": "20+ Artists",
        "duration": "2-Day Event",
        "venue": "Modern Art Gallery",
    },


    9: {
        "title": "Charity Auction Event",
        "type": "Corporate Event",
        "budget": "100000-200000",
        "location": "Salem",
        "venue_type": "Convention Center",
        "image": "images/event9.jpg",

        "short_description":
            "Raising funds for a noble cause with exclusive items.",

        "description":
            "Organize a meaningful charity auction event that brings people together to support important causes.",

        "services": [
            "Auction Management",
            "Guest Registration",
            "Catering",
            "Fundraising Support",
        ],

        "attendees": "500+ Attendees",
        "speakers": "15+ Speakers",
        "duration": "1-Day Event",
        "venue": "Community Convention Hall",
    },


    10: {
        "title": "Food & Wine Tasting",
        "type": "Engagement",
        "budget": "50000-100000",
        "location": "Chennai",
        "venue_type": "Hotel",
        "image": "images/event10.jpg",

        "short_description":
            "A culinary journey with fine wines and gourmet dishes.",

        "description":
            "Experience a premium culinary event featuring gourmet dishes, curated beverages, professional chefs and an elegant atmosphere.",

        "services": [
            "Gourmet Catering",
            "Chef Management",
            "Table Decoration",
            "Guest Management",
        ],

        "attendees": "200+ Guests",
        "speakers": "15+ Chefs",
        "duration": "1-Day Event",
        "venue": "Luxury Dining Hall",
    },


    11: {
        "title": "Name Ceremony",
        "type": "Baby Shower",
        "budget": "50000-100000",
        "location": "Madurai",
        "venue_type": "Banquet Hall",
        "image": "images/event11.jpg",

        "short_description":
            "Memorable and beautiful private celebrations.",

        "description":
            "Celebrate an important family occasion with beautiful decorations, professional catering and complete event coordination.",

        "services": [
            "Traditional Decoration",
            "Catering",
            "Photography",
            "Guest Management",
        ],

        "attendees": "200+ Guests",
        "speakers": "10+ Professionals",
        "duration": "1-Day Event",
        "venue": "Celebration Hall",
    },


    12: {
        "title": "Baby Shower",
        "type": "Baby Shower",
        "budget": "Below-50,000",
        "location": "Salem",
        "venue_type": "Hotel",
        "image": "images/event12.jpg",

        "short_description":
            "A joyful celebration for the upcoming arrival.",

        "description":
            "Celebrate the upcoming arrival of a new family member with a beautiful baby shower.",

        "services": [
            "Baby Shower Decoration",
            "Catering",
            "Games & Entertainment",
            "Guest Management",
        ],

        "attendees": "100+ Guests",
        "speakers": "5+ Professionals",
        "duration": "1-Day Event",
        "venue": "Private Celebration Hall",
    },

}


def home(request):
    return render(request, "index.html")


def events(request):
    return render(
        request,
        "events.html",
        {
            "events": EVENTS
        }
    )


def event_detail(request, event_id):

    event = EVENTS.get(event_id)

    if event is None:
        return render(
            request,
            "404.html",
            status=404
        )

    return render(
        request,
        "event_detail.html",
        {
            "event": event
        }
    )
def book(request):
 return render(request, "book.html")