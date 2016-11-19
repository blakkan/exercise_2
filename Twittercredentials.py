import tweepy

consumer_key = "O8VfG7K4hjDyBMNjk8R7Ds9Jt";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "Gmh90cTMQDg2nQ90YPXE0T65Ww5YkXITSnqeeGSXrG3FrhdaFB";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "797623608935755776-IZieoC8UzUFWgsdHQoowlQwYL0vow2R";

#access_token = "IZieoC8UzUFWgsdHQoowlQwYL0vow2R";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "mwfOIWliEZVm6wT79IPKG1i8KnCz4bZIV3iCaDH9Lcz3D";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
