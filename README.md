# webshotter
Take screenshot of mass domain/subdomains. Light, Fast and best alternative of eyewitness,aquatone etc.

Usage:
1) Clone the repository
2) Install requirements:
 ```pip install -r requirements.txt```
4) Usage Example: ```python3 webshot.py -f {filename} -o {OutputFolder}```

```optional arguments:
  -h, --help        show this help message and exit
  -f , --filename   Name of file containing domains/subdomains
  -o , --output     Name of folder to save the output
  -t , --tabs       Number of tabs to open on browser(Currently in
                    development) (Will be coming soon)
```

If you want to increase speed of screenshot you can do it manually by editing webshotter.py
Steps:-
1) Split the array into dow fast  you want. E.g

```domains = np.array_split(domains, 3) -> change 3 to value you want to (his divides your file to three parts and three parts are processed once to increase speed three times thann usual) ```

2) After step(1) duplicate the code 
```    t3 = mp.Process(target=take_shot, args=(str(2))        t3.start()``` 
 to array times like '```    t4 = mp.Process(target=take_shot, args=(str(3)))      t4.start()``` and join()
 
 Automatic steps will be added soon.
 
 You can contribute to this project.

Contact me at:- sandesharyal.135@gmail.com
