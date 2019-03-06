Packing List
---

*documentation not done yet*

The output from this program outputs to the terminal.
This is done so the user can pipe it to any other software.
For example, it can be used with pandoc and output to many file formats.
```shell
python generate.py -D 5 S m | pandoc -o list.pdf
```
For arguments options, run with the `--help` tag.

You can edit evrything in the config `conf.json`. You can add custom list with a json array and then using the `-C` tag, separating multiple custom lists with a comma.

Heres an example excerpt config file:
```javascript
{
    // other stuff would be here...
    "Military Kit": [
        "gun",
        "more guns",
        "1 used grenade"
    ],
    "Development Kit": [
        "coffee maker",
        "laptop",
        "charger",
        "router"
    ],
    "Fancy Clothing": [
        "suit",
        "red tie",
        "black oxford shoes",
        "belt",
        "watch"
    ]
}
```
You would run all the custom lists with this command
```shell
python generate.py -D 5 -S m -C "Military Kit, Development Kit, Fancy Clothing"
```