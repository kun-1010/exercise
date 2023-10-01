import os
import pydicom
import numpy as np
import nibabel as nib
import torch

# 读取DICOM文件夹路径
dicom_folder = "F:/datasets/kidney_cancer_2023-09-22_06_11_19"

# 创建保存NIfTI文件的目标文件夹
output_folder = "F:/datasets/exercise"
os.makedirs(output_folder, exist_ok=True)

# 遍历DICOM文件夹中的所有.dcm文件
for filename1 in os.listdir(dicom_folder):
    for filename2 in os.listdir(os.path.join(dicom_folder,filename1)):
        print(filename2)
        # if filename.endswith(".dcm"):
        #     dicom_path = os.path.join(dicom_folder, filename)
        #
        #     # 读取DICOM文件
        #     dicom_data = pydicom.dcmread(dicom_path)
        #
        #     # 提取图像数据并转换为PyTorch张量
        #     image_data = dicom_data.pixel_array.astype(np.float32)
        #     image_tensor = torch.from_numpy(image_data)
        #
        #     # 图像数据处理步骤（根据需要进行调整）
        #     # ...
        #
        #     # 创建NIfTI对象
        #     nifti_image = nib.Nifti1Image(image_tensor.numpy(), affine=np.eye(4))
        #
        #     # 保存为nii.gz文件
        #     save_path = os.path.join(output_folder, f"{filename}.nii.gz")
        #     nib.save(nifti_image, save_path)