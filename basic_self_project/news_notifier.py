from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import requests
from plyer import notification

API_KEY = "a5dab0dd1ac64b4b91c85bc871bbe771"
URL = f"https://newsapi.org/v2/top-headlines?sources=techcrunch,the-verge,wired,ars-technica&apiKey={API_KEY}"

class NewsNotifier(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        
        self.label = Label(text="Press the button to get the latest tech news!", size_hint=(1, 0.3))
        self.add_widget(self.label)

        self.button = Button(text="Get News", size_hint=(1, 0.2))
        self.button.bind(on_press=self.show_news)
        self.add_widget(self.button)

    def show_news(self, instance):
        response = requests.get(URL)
        news_data = response.json()
        articles = news_data.get("articles", [])

        if articles:
            top_article = articles[0]  # Get the latest news
            title = top_article["title"][:60] + "..." if len(top_article["title"]) > 60 else top_article["title"]
            description = top_article["description"] or "No description available."
            description = description[:120] + "..." if len(description) > 120 else description

            notification.notify(
                title=title,
                message=description,
                app_name="Tech News Notifier",
                timeout=10
            )
            self.label.text = "Notification sent!"
        else:
            self.label.text = "No news found."

class NewsApp(App):
    def build(self):
        return NewsNotifier()

if __name__ == "__main__":
    NewsApp().run()