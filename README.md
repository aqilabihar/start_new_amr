## Robot Package Template

This is a GitHub template. You can make your own copy by clicking the green "Use this template" button.

It is recommended that you keep the repo/package name the same, but if you do change it, ensure you do a "Find all" using your IDE (or the built-in GitHub IDE by hitting the `.` key) and rename all instances of `my_bot` to whatever your project's name is.

Note that each directory currently has at least one file in it to ensure that git tracks the files (and, consequently, that a fresh clone has direcctories present for CMake to find). These example files can be removed if required (and the directories can be removed if `CMakeLists.txt` is adjusted accordingly).

## Navigasi tujuan titik di peta

Untuk membuat robot bergerak menuju titik yang diklik di peta, ikuti langkah ini:

1. Buat peta area dari world simulasi:
   - Jalankan simulator:
     ```bash
     cd ~/training_ws
     source install/setup.bash
     ros2 launch suraqil_bot launch_sim.launch.py
     ```
   - Jalankan SLAM Toolbox di terminal lain:
     ```bash
     source install/setup.bash
     ros2 launch suraqil_bot slam.launch.py
     ```
   - Gerakkan robot sampai peta terbentuk.
   - Simpan peta ke folder `src/start_new_amr/map`:
     ```bash
     ros2 run nav2_map_server map_saver_cli -f ~/training_ws/src/start_new_amr/map/map
     ```

2. Jalankan Nav2 dengan peta yang sudah dibuat:
   ```bash
   source install/setup.bash
   ros2 launch suraqil_bot nav2.launch.py map:=/home/suraqil/training_ws/src/start_new_amr/map/map.yaml
   ```

3. Buka RViz untuk memberi goal pin point pada peta:
   ```bash
   rviz2
   ```
   - Tambahkan `Map`, `LaserScan`, `TF`, dan `Global Costmap` / `Local Costmap` jika belum muncul.
   - Pakai tool `2D Nav Goal` untuk menempatkan tujuan di peta.

Jika kamu ingin, saya bisa bantu buat launch file RViz yang langsung memuat semua tampilan yang dibutuhkan.

## Master Launcher - Jalankan Semua Sekaligus

Untuk menjalankan simulasi + SLAM + Nav2 + RViz sekaligus, gunakan:

```bash
cd ~/training_ws
source install/setup.bash
ros2 launch suraqil_bot sim_all.launch.py map:=/home/suraqil/training_ws/src/start_new_amr/map/map.yaml
```

### Opsi Master Launcher

- `map`: Path ke file peta YAML untuk Nav2 (default: `src/start_new_amr/map/map.yaml`)
- `enable_slam`: Aktifkan SLAM Toolbox (default: `true`)
- `enable_nav2`: Aktifkan Nav2 navigation (default: `true`)
- `enable_rviz`: Aktifkan RViz visualization (default: `true`)

### Contoh penggunaan dengan opsi

Hanya simulasi + SLAM tanpa Nav2:
```bash
ros2 launch suraqil_bot sim_all.launch.py enable_nav2:=false
```

Simulasi + Nav2 tanpa SLAM (untuk lokalisasi dengan peta yang sudah ada):
```bash
ros2 launch suraqil_bot sim_all.launch.py enable_slam:=false map:=/path/to/map.yaml
```

Semua aktif tapi tanpa RViz:
```bash
ros2 launch suraqil_bot sim_all.launch.py enable_rviz:=false
```
