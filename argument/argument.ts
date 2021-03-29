export class CodeRollerArguments {
    private readonly arguments:Array<string>
    private readonly length:number

    /**
     * @constructor
     * 
     * @param args The command line arguments passed in while
     * running the cli which is passed in for parsing and executing'
     * the commands accordingly
     */
    constructor(args:Array<string>){
        this.arguments = args.slice(2, args.length)
        this.length = this.arguments.length

        this.beginArgumentParser(this.arguments, this.length)
    }

    /**
     * @private
     * 
     * @param argument The arguments
     * @param length The length of the argument
     */
    private beginArgumentParser = (argument:Array<string>, length:number):any => {
        if(length == 0){
            process.exit()
        } else {
            const command = argument[0]
            console.log(argument)
        }
    }
}