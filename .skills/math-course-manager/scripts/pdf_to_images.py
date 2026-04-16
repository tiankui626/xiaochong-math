"""
PDF 转图片脚本
将 PDF 文件转换为 PNG 图片，用于奥数课件处理。

用法：
    python pdf_to_images.py <pdf_path> <output_dir> <prefix>

示例：
    python pdf_to_images.py "第6讲_课后小测.pdf" "附件/第6讲" "课后小测"
"""

import fitz
import os
import sys

def pdf_to_images(pdf_path, output_dir, prefix):
    os.makedirs(output_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=150)
        out_path = os.path.join(output_dir, f"{prefix}_p{i+1}.png")
        pix.save(out_path)
        print(f"  ✓ {os.path.basename(out_path)}")
    doc.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("用法: python pdf_to_images.py <pdf_path> <output_dir> <prefix>")
        sys.exit(1)
    pdf_to_images(sys.argv[1], sys.argv[2], sys.argv[3])
