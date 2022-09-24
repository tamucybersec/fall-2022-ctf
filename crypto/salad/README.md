# Salad
Maaannnnn I'm hungry.
Is there anything to eat?

```
susqy{dafmfuazOubtqdMWMOmqemdOubtqd}
```

## Solution
Based on the title, it's a Casesar cipher, which shifts each letter forward some fixed amount. I just brute-forced different shifts in [CyberChef](https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,false,14)&input=c3VzcXl7ZGFmbWZ1YXpPdWJ0cWRNV01PbXFlbWRPdWJ0cWR9) until I got the flag. Don't forget to rotate the upper-case characters too!

Flag: `gigem{rotationCipherAKACaesarCipher}`
