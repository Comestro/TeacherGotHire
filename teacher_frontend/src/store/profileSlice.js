// import { createSlice } from "@reduxjs/toolkit";

// const initialState = {
//   name: "",
//   email: "",
//   password: "",
//   phone: "",
//   address: "",
//   bio: "",
// };

// const profileSlice = createSlice({
//   name: "profile",
//   initialState,
//   reducers: {
//     updateBasicInfo: (state, action) => {
//       const { name, email, password } = action.payload;
//       state.name = name;
//       state.email = email;
//       state.password = password;
//     },
//     updateAdditionalInfo: (state, action) => {
//       const { phone, address, bio } = action.payload;
//       state.phone = phone;
//       state.address = address;
//       state.bio = bio;
//     },
//   },
// });

// export const { updateBasicInfo, updateAdditionalInfo } = profileSlice.actions;
// export default profileSlice.reducer;

import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  name: "",
  email: "",
  image: "",
  completion: 0, // Profile completion percentage
};

const profileSlice = createSlice({
  name: "profile",
  initialState,
  reducers: {
    updateProfile: (state, action) => {
      const { name, email,image} = action.payload;

      state.name = name || state.name;
      state.email = email || state.email;
      state.image = image || state.image;
      // Update profile completion percentage
      let completionCount = 0;
      if (state.name) completionCount += 33;
      if (state.email) completionCount += 33;
      if (state.image)completionCount +=34
      state.completion = completionCount;
    },
  },
});

export const { updateProfile } = profileSlice.actions;
export default profileSlice.reducer;


