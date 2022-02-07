import PySimpleGUI as sg
from lunardate import LunarDate
list = []
dict = {}
animal = ["Rat","Ox","Tiger","Rabbit","Dragon","Snake","Horse","Sheep","Monkey","Rooster","Dog","Pig"]
gdluck = ["3","9","8","6","5","2","3","7","8","3","4","1"]
bdluck = ["1","7","9","2","6","4","8","2","3","5","9","3"]
day = ["Saturday","Thursday","Tuesday","Friday","Wednesday","Monday","Sunday","Wednesday","Friday","Tuesday","Thursday","Saturday"]
des = ["People born in the Year of the Rat like to think of new and different ways to choose their lucky numbers. Look for inspiration in car license plates or phone numbers.",
"Those born in the year of the Ox spend a lot of time dreaming of winning the lottery instead of playing it. If you decide to play… better go big, as a big jackpot draw will give you millions of incredible dreams, especially when it comes to spending them.",
"Impulsive and impatient… he likes challenges and multiple bets are not scary.",
"There is nothing you enjoy more than laying down, watching your money pile up and grow. Serious increases in your bank account are expected in 2022.",
"Sometimes he likes to bet big and sometimes he doesn't. He is the last to place his bets for the next lottery draw due to the numbers coming to his head at the last minute.",
"Naturally traditional, the Snakes play the same old lotteries. When there is a large jackpot Snakes will make sure they have shared the tickets with their family and friends.",
"Those born in the Year of the Horse dream big and work hard to make dreams come true, but there's nothing wrong with having a little luck when they play. Horses are very generous and they will use the prize money to help the people around, after buying a sports car.",
"Those born in the Year of the Goat are extremely methodical and precise with the selection of their numbers. And they don't forget to rigorously check the results.",
"People born in the Year of the Monkey are aware that all games have their “pros” and “cons”, so in the end, they end up playing all of them. The Horse tries to organize the bets with his friends, comparing his numbers with theirs to make sure that all the winning numbers are evenly divided and distributed among them.",
"As the king of paranoia, you already have your “escape plan” in place for the day when luck strikes you. It is so mysterious that it is difficult to know what your favorite lottery games are.",
"In search of new experiences, you will often be traveling. Their motto is 'play big or go home!'",
"Those born in the Year of the Pig are ambitious but also conservative, which is why they prefer traditional games where they don't have to waste a lot of time choosing numbers."]
def clear_input():
    for key in values:
        if key != 'Date':   
            window[key]('')
    return None 
def homepage():

    layout = [
        [sg.Text('Enter Your Birthday ', size=(20,1)), sg.InputText(key='value')],
        [sg.Button('Enter'), sg.Button('Clear'), sg.Exit()]
    ]      

    return sg.Window('Generate Client Profile', layout,element_justification='c', default_element_size=(100, 1), auto_size_text=False, auto_size_buttons=False,      
                     default_button_element_size=(12, 1), size=(600,270), finalize=True)

def nextpage():

    layout = [        
        [sg.Text('Your Lunar Birthday is (DD MM YYYY): ', size=(30,1)), sg.Input(str(list[0])+" "+(str(list[1]))+" "+(str(list[2])), readonly=True)],
        [sg.Text('Your Animal is: ', size=(20,1)), sg.Input(animal[b], readonly=True)],
        [sg.Text('Your lucky number is: ', size=(20,1)), sg.Input(gdluck[b], readonly=True)],
        [sg.Text('Your unlucky number is: ', size=(20,1)), sg.Input(bdluck[b], readonly=True)],
        [sg.Text('Your lucky day is: ', size=(20,1)), sg.Input(day[b], readonly=True)],
        [sg.Text(des[b], size=(50,5))],
        [sg.Exit()]
    ]          

    return sg.Window('Generate Client Profiles', layout,element_justification='c', default_element_size=(100, 1), auto_size_text=False, auto_size_buttons=False,      
                     default_button_element_size=(12, 1), size=(600,270), finalize=True)



window1, window2= homepage(), None 
while True:      
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'Exit' or event =='Close' or event =='Log out of Current Company':
        window.close()
        if window == window2:
            window2 = None
    
    elif event == 'Enter':
        if values['value'] == '':
            sg.popup('You must specify your birthday', title="Error")
        else:
            values['value'] = (str(values['value']))
            value = values['value']
            value= value.split(" ")
            a = LunarDate.fromSolarDate(int(value[2]),int(value[1]),int(value[0]))


            b = a.year
            b = b-1900
            b = b%12
            if (a.month <10):
                a.month = str(a.month)
                a.month = "0"+ a.month
            list = [a.day,a.month,a.year]
            window = nextpage()
    elif event == 'Clear':
        clear_input()