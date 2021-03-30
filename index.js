require('dotenv').config();

const Discord = require('discord.js');
const Shorten = require('./shorten.js');
const bot = new Discord.Client();

// the environment variables
const TOKEN = process.env.TOKEN;
const URL = process.env.URL

// login as a bot
bot.login(TOKEN);

bot.on('ready', () => {
    console.info(`Logged in as ${bot.user.tag}!`);
});


bot.on('message', msg => {
    // make sure that the message is
    // a command for the shurl bot
    const command = msg.content.startsWith("^shurl")
    if (command) {
        // split the content so that we only take the first
        // element or the firslt link in the message
        let url = msg.content.toString().split(" ")
        url = url.slice(1, url.length)
        if (url.length == 0) {
            // if the user enters no url, return 
            // a slight_smile to the user :wink:
            msg.reply(":slight_smile:")
        } else {
            // shorten the url
            const shortener = new Shorten(url[0]).createShortenedUrl(URL, msg)
            console.log(shortener)

        }
    }
});