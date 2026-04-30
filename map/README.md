# Map Folder

Simpan peta yang sudah dibuat di folder ini.

Contoh nama file peta yang digunakan oleh nav2:

- map.yaml
- map.pgm

Setelah memetakan area dengan SLAM Toolbox, simpan peta dengan:

```bash
ros2 run nav2_map_server map_saver_cli -f ~/training_ws/src/start_new_amr/map/map
```
