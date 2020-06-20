/*
判断是否包含特殊字符
*/
export function stripscript(s) {
  // var pattern = new RegExp("[`~!@#$^&*()=|{}':;',\\[\\].<>/?~！@#￥……&*（）&;—|{ }【】‘；：”“'。，、？]")
  // let rs = "";
  // for (var i =0; i < s.length; i++){
  //     rs = rs + s.substr(i, 1).replace(pattern, '');
  // }
  // return rs;
  // 上面是去掉特殊字符

  var reg = RegExp(
    "[`~!@#$^&*()=|{}':;',\\[\\].<>/?~！@#￥……&*（）&;—|{ }【】‘；：”“'。，、？]"
  );
  if (s.match(reg)) {
    // 包含： 返回false
    return false;
  } else {
    return true;
  }
}

export function getUrlKeyQ(name) {
  return (
    decodeURIComponent(
      (new RegExp("[?|&]" + name + "=" + "([^&;]+?)(&|#|;|$)").exec(
        location.href
      ) || [, ""])[1].replace(/\+/g, "%20")
    ) || null
  );
}
