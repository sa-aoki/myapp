    // os-btnというidを持つHTML要素を取得し、定数に代入する
    const select = document.querySelector('select');
    const options = select.options; 
    // HTML要素がクリックされたときにイベント処理を実行する
    // すべてのチェックボックスを配列風のデータで取得する
    const items = document.select.project_info.select.project_info; 
    
    // 繰り返し処理でチェックボックスを1つずつ取り出し、もし選択されていれば値を出力する
    for (let i = 0; i < items.length; i++) {
        if (items[i].selected) 
        console.log(items[i].value); 
    }