# EduMap GIS — Vietnam Higher Education Dashboard

Dashboard WebGIS tra cứu cơ sở giáo dục đại học Việt Nam. © 2026 Long Ngo, giấy phép MIT.

## Chức năng
- Tìm kiếm không dấu, lọc loại hình/cơ quan quản lý/địa điểm, biểu đồ thống kê động.
- Bản đồ Leaflet, chuyển nền OpenStreetMap / Esri World Imagery.
- Vòng tròn theo địa điểm chỉ thể hiện số cơ sở ở vị trí đại diện, **không phải điểm khuôn viên**.
- Nạp FeatureCollection GeoJSON chứa Point WGS84 với thuộc tính `name` khớp tên trong danh mục, hiển thị điểm chính xác.
- Xuất CSV danh mục hoặc GeoJSON các điểm có tọa độ đã nạp.
- Ranh giới 34 tỉnh từ Cloudflare R2 tham chiếu ClipMap, chỉ tải khi bật (phụ thuộc URL công khai và CORS).

## Trạng thái dữ liệu
Tệp `data/universities.json` gồm **51 bản ghi ví dụ** trích từ HTML do người dùng cung cấp. Con số **226** là mục tiêu danh mục, **không phải** 226 hồ sơ đã xác thực. Trường dữ liệu `area`, `scale`, `manager`, `type` và `founded` là dữ liệu minh họa chưa xác minh độc lập và có thể không phản ánh cơ cấu tổ chức mới. Không tự sinh thêm 175 tên trường hoặc tọa độ.

Thay `data/universities.json` bằng danh mục 226 cơ sở đã kiểm chứng. Để hiển thị điểm trường chính xác, nạp GeoJSON Point (EPSG:4326), thuộc tính `name` phải trùng với trường `name` trong danh mục.

## Chạy
Mở bằng GitHub Pages: https://xulytiengviet.github.io/edumap/ (sau khi kích hoạt Pages: GitHub Actions).
Chạy nội bộ bằng web server tĩnh, chẳng hạn `python -m http.server 8000`. Không cần backend.

## Nguồn tham khảo
- https://github.com/xulytiengviet/clipmap
- https://github.com/Vietflexmap/anhmap

Thư viện và ảnh nền của bên thứ ba theo giấy phép riêng. Ghi công OpenStreetMap contributors và Esri theo nguồn.
