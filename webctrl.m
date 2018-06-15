

function [resp] = webctrl(theta, V)

url = 'http://192.168.0.188:5000/receiver';

options = weboptions('RequestMethod', 'post');

resp = webwrite(url,'angle', num2str(int32(theta)), 'speed', num2str(int32(V)), options);

end
