from __future__ import absolute_import, print_function
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

consumer_key="7t5IKP5fVr89wkd86440g3eKX"
consumer_secret="d9pQ8mMlmeBN8KkPZgD4KL4FHsTwrkQ3oH0KNeZqUgZg4rqZC9"
access_token="1176352760742260736-21iQ0H09I8cGjKIXnhIGN16DXVcQiJ"
access_token_secret="Mz62wIy8jJJbLgyVw3LPXL5fWKVF7KF4Dg0LsjXh6hcMI"

class StdOutListener(StreamListener):
    def on_data(self, data):
        try:
            with open('data10.json', 'a') as outfile:
                json.dump(data,outfile)
            with open('data20.json','a') as outputj:
                outputj.write(data)
            with open('tweetsdata.txt', 'a') as tweets:
                tweets.write(data)
                tweets.write('\n')
            outfile.close()
            tweets.close()
            outputj.close()
        except BaseException as e:
            print('problem collecting tweet',str(e))
        return True
    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['WHO','CovidVaccine','Covid19Vaccine','Covid20Vaccine','Covid19','AstraZeneca','Moderna','ThisIsOurShot','MaskUp','Vaccinated','GetVaccinated','Vaccines','Covaxin','Covishield','VaccineWastage','Vaccine','Pfizer','Covid19Vaccination','VaccineDrive','covid','JNJ','CoviShield','VaccinationDrive','BharatBioTech','CoronaVaccine','Biontech','PfizerBiontech','sinopharm','sinovac','SputnikikV','Covax','OxfordAstraZeneca','Johnson & Johnson','CovishieldVaccine'])