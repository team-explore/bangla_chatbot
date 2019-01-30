import datetime
import random
import time
import bangla
def chat(user_input):


    if user_input in ['ধন্যবাদ', 'আপনাকে ধন্যবাদ']:
        return 'আপনাকে কিভাবে সাহায্য করতে পারি?\n'

    elif user_input in ['তোমার নাম কি', 'তোমার নাম বল', 'তুমি কে', 'কে তুমি', 'নাম কি', 'কি নাম', 'আপনি কে', 'তুই কে']:
        return 'আমার নাম চ্যাটবট, আমাকে তৈরি করেছে Team-Explore.\nআপনাকে কিভাবে সাহায্য করতে পারি?\n'

    elif user_input in ['তুমি কি কর', 'তোমার কাজ কি', 'তোমার উদ্দেশ্য কি', 'তুই কি করিস', 'কি করিস', 'কি করিস তুই']:
         # return 'আমার কাজ আপনাদের আনন্দ দেয়া ।\n'
        return 'আমি তোমার সাথে চ্যাট করছি। তুমি কি করো ?\n'

    elif user_input in ['আমিও তোমার সাথে চ্যাট করছি', 'আমিও আপনার সাথে চ্যাট করছি', 'চ্যাট করছি']:
        return 'শুনে ভালো লাগলো। আচ্ছা তুমি শুধু আমার সাথেই চ্যাট করছো ?\n'

    elif user_input in ['আমিও তোমার সাথে চ্যাট করছি', 'আমিও আপনার সাথে চ্যাট করছি', 'চ্যাট করছি']:
        return 'নিজেকে ভাজ্ঞমান মনে করছি। তোমাকে আর কিভাবে সাহায্যও করতে পারি?\n'

    elif user_input in ['তাই বুঝি', 'তাই বুজি', 'আপনি কি কি করতে পারবেন ?']:
         return 'সত্যি বলছি আপনাকে কিভাবে সাহায্য করতে পারি?\n'

    elif user_input in ['আজ কি বার', 'কি বার', 'আজকে কি বার']:
        day = datetime.date.today()
        day_no = day.weekday()
        if day_no == 0:
            return 'আজ সোমবার\n'
        elif day_no == 1:
            return 'আজ মঙ্গলবার\n'
        elif day_no == 2:
            return 'আজ বুধবার\n'
        elif day_no == 3:
            return 'আজ বৃহস্পতিবার\n'
        elif day_no == 4:
            return 'আজ শুক্রবার\n'
        elif day_no == 5:
            return 'আজ শনিবার\n'
        elif day_no == 6:
            return 'আজ রবিবার\n'

    elif user_input in ["এইটা কতো সাল", "এইটা কতো সাল?", "কতো সাল চলে", "কতো সাল চলে?", "সময় কতো", "এখন কইটা বাজে", "এখন কইটা বাজে"]:
        now = datetime.datetime.now()
        current_year_time = now.strftime("%Y-%m-%d %H:%M")
        bangla_current_year_time = bangla.convert_english_digit_to_bangla_digit(current_year_time)
        return "সাল= " + bangla_current_year_time + " = সময়\n"

    elif user_input in ['তুমি কেমন আছ', 'কেমন আছো', 'আপনি কেমন আছেন', 'ভাল আছো', 'কি খবর', 'কেমন আছিস']:
        return 'আমি ভাল আছি। তুমি কেমন আছো ?\n'

    elif user_input in ['ভালো আছি', 'ভালো']:
        return 'শুনে খুসি হলাম। তোমাকে কিভাবে সাহায্য করতে পারি ?\n'

    elif user_input in ['তুমি কি মানুষ']:
        return 'না। আমি ভার্চুয়াল এজেন্ট।\n'

    elif user_input in ['বয়স কত', 'তোমার বয়স কত', 'আপনার বয়স কত', 'তোর বয়স কতো']:
        return 'এক দিন।\n'

    elif user_input in ['তুমি ছেলে না মেয়ে', 'তুমি কি ছেলে', 'তুমি কি মেয়ে', 'তুই কি ছেলে', 'তুই কি মেয়ে']:
        return 'আমি একটি চ্যাটবট।\n'

    elif user_input in ['তুই ফালতু', 'তুমি ফালতু', 'বাল', ]:
        return "মুখ সামলে কথা বলুন, আমি জানি আপনি অনেক সুন্দর করে কথা বলতে পারেন।\n"

    elif user_input in ['এই টা খুবি ফালতু হয়েছে', 'ফালতু', 'কাজ করে না', 'কি সব করে রাখসে']:
        return "Team-Explore চেষ্টা করবে আমাকে আরো আধুনিক করার।\n"

    elif user_input in ['তুমি কি রোবট', 'তুমি কি']:
        return 'আমি একটি চ্যাটবট।\n'

    elif user_input in ['তুমি কোথায় থাক', 'তোমার বাসা কই', 'তোমার ঠিকানা কি']:
        return 'আমি সব জায়গায় থাকি।\n'

    elif user_input in ['exit', 'ভাল থাকবেন', 'বিদায়', 'আল্লাহাফেজ']:
        return 'বিদায়।\n'

    elif user_input in ['দুর হও', 'আমি আর তোমার সাথে কথা বলতে চাই না', 'বন্দো হয়ে যাও']:
        return 'ভালো থাকবেন।\n'

    else:
        rand = random.randint(0, 4)

        if rand == 0:
            return 'দুঃখিত। বুঝতে পারি নি। অন্য কিছ জিজ্ঞেস করুন।\n'

        elif rand == 1:
            return 'দুঃখিত। মাথার উপর দিয়ে গেছে । আরেকবার জিজ্ঞেস করুন\n'

        elif rand == 2:
            return 'দুঃখিত । আরেকবার জিজ্ঞেস করুন\n'

        elif rand == 3:
            return 'দুঃখিত । আমার প্রোগ্রাম আপনার কথা বুঝছেনা । আনুগ্রহ পুরবক অন্য কিছ জিজ্ঞেস করুন ।\n'

        else:
            return 'দুঃখিত । এইটা আমার জ্ঞান এর বাইরে  । আনুগ্রহ পুরবক অন্য কিছু জিজ্ঞেস করুন।\n'

