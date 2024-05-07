import * as React from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';

const Content = () => {
    return (
      <>
        <Box sx={{"width" : "40%", "marginLeft" : "35rem"}}> 
          <Typography variant="h1" sx={{"marginTop" : "5rem"}}>
          Sign Lingua with Nashtech
          </Typography>
          <Typography variant='h6' sx={{"marginTop" : "5rem"}}>
          Where people can convey their thoughts everyone seamlesly.
          </Typography>
          <Typography variant="h3" sx={{"marginTop" : "2rem"}}>
            Are you facing problem to share your ideas or it is difficult for others to understand your thoughts ?
          </Typography>
          <Typography variant="h5" sx={{"marginTop" : "2rem"}}>
          We're developing a sign language translator to support the verbally challenged and deaf community. Our solution aims to seamlessly translate sign language into spoken or written language, enabling
silent and deaf individuals to communicate with anyone regardless of their knowledge of sign language. By leveraging advanced technology, including computer vision and machine learning, our solution will empower such  individuals to express themselves effectively
- Dependency on interpreters can be eliminated by educating other individuals about basics of sign language
- Providing the manual for sign language
- Integration with multiple platforms (like teams, meet etc)
- An online community for deaf and mute people where they can share their thoughts and ideas with each other
- Provide customization option for users (like American Sign language(ASL), Indian Sign Language (ISL) etc)
- Easy to use technology for removing technology barrier
          </Typography>
        </Box>
      </>
    );
  };
  
  export default Content;
  