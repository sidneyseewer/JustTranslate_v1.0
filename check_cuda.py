import torch

def check_cuda():
    print("Checking CUDA installation...\n")
    
    # Check if CUDA is available
    if torch.cuda.is_available():
        print("CUDA is available!")
        
        # Get CUDA version
        print(f"CUDA Version: {torch.version.cuda}")
        
        # Get number of available GPUs
        gpu_count = torch.cuda.device_count()
        print(f"Number of GPUs detected: {gpu_count}")
        
        for i in range(gpu_count):
            gpu_name = torch.cuda.get_device_name(i)
            gpu_capability = torch.cuda.get_device_capability(i)
            print(f"GPU {i}: {gpu_name}")
            print(f"  Compute Capability: {gpu_capability}")
        
        # Check default device
        default_device = torch.cuda.current_device()
        print(f"\nDefault GPU in use: {torch.cuda.get_device_name(default_device)}")
    else:
        print("CUDA is not available. Please check your installation.")

if __name__ == "__main__":
    check_cuda()
