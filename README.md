# low-resolution-proc

## Usage
The first argument is the window size.\
The second argument is the number of colors.\
If the number of the first argument is increased, the generated image becomes blurred.\
If the number of the second argument is decreased, the color representation of the generated image becomes monotonous.

### example1 \
```python low-resolution-proc.py sample.png out.png 3 122```

![image](https://user-images.githubusercontent.com/55880071/187933165-84ad6721-fbce-4e35-98ba-b90df5a74fc9.png)

### example2 \
```python low-resolution-proc.py sample.png out.png 3 5```

![image](https://user-images.githubusercontent.com/55880071/187934007-7f6a2a6e-53bb-40ef-a279-f7e816459054.png)


### example3 \
```python low-resolution-proc.py sample.png out.png 7 122```

![image](https://user-images.githubusercontent.com/55880071/187933751-b7370e3f-da2e-4168-b05b-a1aee5b79c18.png)
