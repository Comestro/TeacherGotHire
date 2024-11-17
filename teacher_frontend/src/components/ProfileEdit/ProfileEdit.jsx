import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { updateProfile } from "../../store/profileSlice";
import { useNavigate } from "react-router-dom";
import Input from "../Input";
import { useForm } from "react-hook-form";
import Button from "../Button";
import Navbar from "../Navbar/Navbar";
import ProfileButton from '../Profile_Button/Profile_Button';

const ProfileEdit = () => {
  // const dispatch = useDispatch();
  const navigate = useNavigate();
  const { register, handleSubmit,watch } = useForm();
  const [error, setError] = useState('');
  const [preview, setPreview] = useState(null);
  // const profile = useSelector((state) => state.profile);


  const handleImagePreview = (file) => {
    const reader = new FileReader();
    reader.onload = () => {
      setPreview(reader.result); // Base64 string
    };
    reader.readAsDataURL(file);
  };

  const EditPortfolio = async (data)=>{
    console.log(data);
    //send data from here to backend
  }

  // Watch for changes to the file input
  const watchImage = watch("image");
  if (watchImage && watchImage.length > 0) {
    handleImagePreview(watchImage[0]);
  }



  return (
    <>
    <nav>
    <div className=''>
          <Navbar
              links={[
                  {id:'1', label: "Contact US", to: "/contact" },
                  {id:"2", label: "AboutUs", href: "/about" },
                ]}
                variant="dark"
                // notifications={notifications}
                externalComponent={ProfileButton}
              />
        </div>
    </nav>
    <div className="max-w-lg mx-auto p-4 bg-white shadow rounded-md">
      <h2 className="text-xl font-bold mb-4">Edit Profile</h2>
      {error && (
          <p className="text-red-600 text-center mb-4">{error}</p>
        )}
        
                <form onSubmit={handleSubmit(EditPortfolio)} className="space-y-6">
                <Input
                  label="Full Name"
                  placeholder="Enter your full name"
                  {...register('name', { required: true })}
                />
                <Input
                label="Email"
                placeholder="Enter your Address"
                />
                <Input
                label="Full Address"
                placeholder="Enter your Address"
                />
                <Input
                label="Phone number"
                placeholder="Enter your phone number"
                {...register('name', { required: true })}
                />
                <Input
                label = "Upload file"
                type="file"
               {...register("image", {
                  required: true,
                  validate: (file) => file[0]?.size < 5 * 1024 * 1024 || "File size should be less than 5MB",
                })}
                accept="image/*" />
                        {preview && (
                  <div className="mb-4">
                    <img src={preview} alt="Preview" className="w-32 h-32 rounded-full" />
                  </div>
                )}
                <Button>
                  Upadte Profile
                </Button>

                </form>
    </div>
    </>
    
  );
};

export default ProfileEdit;
