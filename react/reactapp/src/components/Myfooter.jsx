
import { Footer, FooterCopyright, FooterLink, FooterLinkGroup } from "flowbite-react";

export default function Myfooter() {
  return (
    <Footer container className="bg-sky-800 ">
      <FooterCopyright className="text-white" href="#" by="ReactApp™" year={2022} />
      <FooterLinkGroup className="text-white">
        <FooterLink href="#">About</FooterLink>
        <FooterLink href="#">Privacy Policy</FooterLink>
        <FooterLink href="#">Licensing</FooterLink>
        <FooterLink href="#">Contact</FooterLink>
      </FooterLinkGroup>
    </Footer>
  );
}
