const request = require("request");
const Discord = require('discord.js');

class Shorten {
    static url = "https://api.rebrandly.com/v1/links"

    constructor(url){
        this.url = url
    }

    createRequestLinks = (url) => {
        return {
            destination: url.toString(),
            domain: { fullName: "rebrand.ly" }
        }
    }

    createShortenedUrl = (apiKey, msg) => {
        request({
            uri : "https://api.rebrandly.com/v1/links",
            method : "POST",
            body : JSON.stringify(this.createRequestLinks(this.url)),
            headers : {
                "Content-Type": "application/json",
                "apikey": apiKey,
            }
        }, (error, response, body) => {
            let link = JSON.parse(body)
            let Embed = new Discord.MessageEmbed()
                .setTitle("Shul")
                .setDescription(`Here is your url - ${link.shortUrl}`)
            msg.reply(Embed)
            return link.shortUrl
        })   
    }
}

module.exports = Shorten