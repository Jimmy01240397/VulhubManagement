var allvulns = null

axios
  .get('/list')
  .then((res) => {
    allvulns = res.data
    var ul = document.getElementById('allvulns')

    allvulns.forEach(function (item, i) {
      var li = document.createElement('li')
      ul.appendChild(li)
      var form = document.createElement('form')
      form.method = 'GET'
      form.action = `/vuldetail/${item.split('/')[2]}`
      var id = item
      li.appendChild(form)
      var path = document.createElement('input')
      path.type = 'hidden'
      path.name = 'path'
      path.value = item
      form.appendChild(path)
      var bt = document.createElement('button')
      bt.type = 'submit'
      bt.innerHTML = item.split('/')[2]
      form.appendChild(bt)
    })
  })
  .catch((err) => {
    console.log(err)
  })
