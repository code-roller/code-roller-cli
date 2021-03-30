require('dotenv').config();

const Discord = require('discord.js');
const Shorten = require('./shorten.js');
const bot = new Discord.Client();


const TOKEN = process.env.TOKEN;
const URL = process.env.URL

bot.login(TOKEN);

bot.on('ready', () => {
    console.info(`Logged in as ${bot.user.tag}!`);
});


bot.on('message', msg => {
    const command = msg.content.startsWith("^shurl")
    if(command){
        let url = msg.content.toString().split(" ")
        url = url.slice(1, url.length)
        if(url.length == 0){
            msg.reply(":slight_smile:")
        } else {
            const shortener = new Shorten(
                url[0], URL
            )
            msg.reply(url[0])
        }
    }
});