
 import bannerimg from '../assets/banner.jpg'

// const MyBanner = () => {
//     return(
//         <section className='banner'>
//             <img src={bannerimg} alt="" />
//         </section>
//     )
// }
// export default MyBanner


import {Banner, BannerCollapseButton } from "flowbite-react";
// import { HiX } from "react-icons/hi";
// import {MdAnnouncement} from "react-icons/md"


export default function MyBanner(){
    return (
        <Banner> 
            <img src={bannerimg} alt="" className='h-[500px] w-full'/>
        </Banner>
    );
}