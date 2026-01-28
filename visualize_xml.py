import mujoco
import mujoco.viewer
import os

# 1. Save your XML content to a file in the directory where your includes are
# (Or just point this path to your existing .xml file)
xml_path = '/home/stevexing/act/assets/bimanual_viperx_ee_pp_socket_cube.xml'

def main():
    if not os.path.exists(xml_path):
        print(f"Error: {xml_path} not found. Please save your XML first.")
        return

    # 2. Load the model and data
    model = mujoco.MjModel.from_xml_path(xml_path)
    data = mujoco.MjData(model)

    # 3. Launch the interactive viewer
    # This will open a window where you can see the arms and the box.
    mujoco.viewer.launch(model, data)

if __name__ == "__main__":
    main()