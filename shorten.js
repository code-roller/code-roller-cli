const request = require("request");
const Discord = require('discord.js');

class Shorten {
    static url = "https://api.rebrandly.com/v1/links"

    /**
     * @constructor
     * @param {String} url The url to shorten  
     */
    constructor(url){
        this.url = url
    }

    /**
     * 
     * @param {String} url The url to shorten 
     * @returns an object with some properties
     *  - (destination) - The url
     *  - (domin) - The domain of the shortened url
     */
    createRequestLinks = (url) => {
        return {
            destination: url.toString(),
            domain: { fullName: "rebrand.ly" }
        }
    }

    /**
     * Fetched the the shortened url from the api and reply
     * the user with an embed
     * 
     * @param {String} apiKey The rebrand api key to request the server
     * for a shortened url 
     * @param {MessageChannel} msg The discord message channel to send 
     * a reply to the user 
     */
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
            const image = "https://raw.githubusercontent.com/code-roller/package-manager/main/assets/shurl.jpg"
            let link = JSON.parse(body)
            const short = `https://${link.shortUrl}`
            let Embed = new Discord.MessageEmbed()
            .setColor('#7289DA')
            .setTitle('Here is your url')
            .setURL(short)
            .setAuthor('Shurl', image, 'https://raw.githubusercontent.com/code-roller/package-manager/main/assets/shurl.jpg')
            .setDescription(`Your shortened url-${short} :slight_smile:`)
            .setThumbnail(image)
            msg.reply(Embed)
            return link.shortUrl
        })   
    }
}

module.exports = Shorten