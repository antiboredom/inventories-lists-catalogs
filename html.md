# Inventories, Lists and Catalogs

Pioneer Works, 2016


## What's a website?

### HTML

HTML is "hypertext markup language". HTML is made up of a set of tags that define structure and meaning.

Here's what a basic html document might look like:

```html
<html>
	<head>
		<title>A Spectre is Haunting Europe</title>
	</head>
	
	<body>
		<p>Greetings Comrade!</p>
	</body>
</html>
```

Some tags wrap around other content (either text or other tags), and some tags exist on their own.

Some important tags:

```<html><html>```

```<p>I'm a paragraph</p>```

```<img src="trotsky.jpg">```

```<a href="http://pravda.ru">Click here!</a>```

![](https://camo.githubusercontent.com/75a02359b7d1e48f52f2012c91bdee4e9cb60a94/68747470733a2f2f6d646e2e6d6f7a696c6c6164656d6f732e6f72672f66696c65732f373635392f616e61746f6d792d6f662d616e2d68746d6c2d656c656d656e742e706e67)


#### Tag attributes

Tags can have attributes associated with them. Some attributes can only apply to certain elements (like img src), other can be applied to any element, like ```id``` and ```class```


```id``` ids must be unique - ie only one element on a page can have a particular id

```class``` a category or "class" of element. Multiple elements can have the same class.

For example:

```html
<h1 id="logo">The logo for the site goes here">LOGO</h1>

<p class="big-paragaph">The first big paragraph</p>
<p class="big-paragaph">The second big paragraph</p>
```

### CSS

CSS stands for "cascading style sheet". It gives as a way to format or "style" HTML.

We can add style to HTML elements by referencing their tag names, ids, or classnames.

To style an element, just use it's tag name. To style an element with a particular id, use it's id name preceeded with the ```#``` character. To style a series of elements that share a class, reference the class name, preceeded with a ```.```

```css

/* make paragraphs have bold text */
p {
	font-weight: bold;
}

/* make the element that has the id "logo" have a thick red border around it
#logo {
	border: 10px solid red;
}

/* make all elements with the "big" class have giant text */
.big {
	font-size: 100px;
}

```

We can also style elements inside of other elements.

It's not important to know what all the possible CSS styles are, just how to reference elements using CSS - we'll be using this when we start web scraping.


### The Web Inspector

How to use the chrome web inspector...


