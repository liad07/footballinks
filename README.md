```javascript
fetch("https://footballinks.pythonanywhere.com/?channel=55")
            .then(response => response.json())
            .then(data =>console.log(data.num+","+data.name+","+data.ename+","+data.janerr+","+data.link))
```
