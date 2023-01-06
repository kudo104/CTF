# ctf_challenge
Tác giả cho 2 file ctf_challenge và flag.txt.Đây là một dạng bài phục hồi lại nội dung trong file.

![alt](http://~)

Bỏ vào ida thì biết được chương trình đọc nội dung flag.txt để encrypt

![alt](http://~)

Tạo file flag.txt và thử thêm nôi dụng là `ASCIS{aaaaaaaaa}` để chạy file. Hmm nhìn khá là ảo thử lấy đống hex này sang string thử ,chương trình lại cho ra đúng nội dung của flag.

![alt](http://~)

Tiếp tục re tiếp thì bài này là một dạng vm mình sẽ không nói chi tiết mấy cái này tại thấy dài dòng quá.Bài này cấp phát một vùng nhớ 50 byte có quyền thực thi và set cái tất cả các byte trong vùng nhớ thành 0x90 đây chính là lệnh nop và thêm 2 byte ``\xEB\xFE`` này vào vùng nhớ gần cuối đây chính là lệnh jump nhảy tới chính nó đó.Sau đó nó sẽ tạo Thread vô tận đợi đến khi mà chương trình gọi ``SuspendThread`` để tạm dừng Thread lại.Sau đó chương trình sẽ tính toán và sẽ thực thi từng câu lệnh một trong vùng nhớ này.



Đang chú ý trong quá trình debug thì mình bị lỗi segment liên tục thì phát hiện có 1 anti hardware breapoint

![alt](http://~)

Đến đây mình patch lại chương trình tưởng có thể chạy ngon lành cành đào rồi nhưng không nó lại in ra đúng nối dung của file flag.txt.Mình thử debug tới câu lệnh cuối cùng trong vùng nhớ rồi in ra thì biết được nó tính độ dài của chuỗi và so sánh với 0x24.Hmm chạy ngon rồi haha.

![alt](http://~)

Mình sử dụng mấy câu lẹnh debug_hook của ida không chạy được nên đành chạy tay lấy từng câu lệnh một click đến khi nào chương trình dừng thì thôi do mình lười emulate lại cái code vm :vv

![alt](http://~)

Sau khi đọc mấy cái code vm này thì biết được đây là mã hóa ``XTEA``

Flag: ``ASCIS{M@sT3r_0f_V1rtu4l_m4Ch1n3}``