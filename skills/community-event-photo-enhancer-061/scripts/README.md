# 本地离线图片优化脚本

`optimize_photos.py` 使用 Pillow 和 NumPy 执行本地曝光、温和白平衡、对比度、降噪、锐化和尺寸优化。原图不会被覆盖。

```bash
python optimize_photos.py --input-dir ./input --output-dir ./output --max-width 1280 --quality 88
```

支持JPEG、PNG、WEBP。输出目录会生成 `processing_record.json`。只有脚本实际运行并输出可打开文件时，才能声称已完成图片处理。
