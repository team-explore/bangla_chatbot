import datetime

def bot():
    print("Bot: আপনাকে স্বাগতম।")

    while(True):

        user_input = input('Me: ')
        print('Bot:', end=' ')

        if user_input in ['ধন্যবাদ', 'আপনাকে ধন্যবাদ']:
            print('আপনাকে কিভাবে সাহায্য করতে পারি?\n')

        elif user_input in ['তোমার নাম কি', 'তোমার নাম বল', 'তুমি কে', 'কে তুমি', 'নাম কি', 'কি নাম']:
            print('আমার নাম অমুক।\n')

        elif user_input in ['আজ কি বার', 'কি বার', 'আজকে কি বার']:
            day = datetime.date.today()
            day_no = day.weekday()
            if day_no == 0:
                print('আজ সোমবার')
            elif day_no == 1:
                print('আজ মঙ্গলবার')
            elif day_no == 2:
                print('আজ বুধবার')
            elif day_no == 3:
                print('আজ বৃহস্পতিবার')
            elif day_no == 4:
                print('আজ শুক্রবার')
            elif day_no == 5:
                print('আজ শনিবার')
            elif day_no == 6:
                print('আজ রবিবার')

        elif user_input in ['তুমি কেমন আছ', 'কেমন আছো', 'আপনি কেমন আছেন', 'ভাল আছো', 'কি খবর']:
            print('আমি ভাল আছি। আমাকে প্রশ্ন করুন।')

        elif user_input in ['তুমি কি মানুষ']:
            print('না। আমি ভার্চুয়াল এজেন্ট।')

        elif user_input in ['বয়স কত', 'তোমার বয়স কত', 'আপনার বয়স কত']:
            print('এক দিন।')

        elif user_input in ['তুমি ছেলে না মেয়ে', 'তুমি কি ছেলে', 'তুমি কি মেয়ে']:
            print('আমি মানুষ না।')

        elif user_input in ['তুমি কি রোবট', 'তুমি কি']:
            print('আমি একটি চ্যাটবট।')

        elif user_input in ['তুমি কোথায় থাক', 'তোমার বাসা কই', 'তোমার ঠিকানা কি']:
            print('আমি সব জায়গায় থাকি।')

        elif user_input == 'exit':
            print('বিদায়।')
            break

        else:
            print('দুঃখিত। বুঝতে পারি নি। অন্য কিছু জিজ্ঞেস করুন।')


if __name__ == '__main__':
    bot()