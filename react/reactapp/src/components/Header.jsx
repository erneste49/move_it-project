// const Header = () => {
//     return(
//        <nav className="nav">
//             <h1 className="bg-white text-sky-500 text-2xl font-bold px-5 py-3">Logo</h1>
//             <ul>
//                 <li><a href=""> Home </a></li>
//                 <li><a href=""> About</a></li>
//                 <li><a href=""> Contact</a></li>
//                 <li><a href=""> Services</a></li>
//             </ul>
//        </nav>
//     )
// }
// export default Header



import { Button, Navbar, NavbarBrand, NavbarCollapse, NavbarLink, NavbarToggle } from "flowbite-react";

export default function Header() {
  return (
    <Navbar fluid rounded>
      <NavbarBrand href="https://flowbite-react.com">
        <img src="/favicon.svg" className="mr-3 h-6 sm:h-9" alt="Flowbite React Logo" />
        <span className="self-center whitespace-nowrap text-xl font-semibold dark:text-white">React App</span>
      </NavbarBrand>
      <div className="flex md:order-2">
        <Button>Get started</Button>
        <NavbarToggle />
      </div>
      <NavbarCollapse>
        <NavbarLink href="#" active>
          Home
        </NavbarLink>
        <NavbarLink href="#">About</NavbarLink>
        <NavbarLink href="#">Services</NavbarLink>
        <NavbarLink href="#">Pricing</NavbarLink>
        <NavbarLink href="#">Contact</NavbarLink>
      </NavbarCollapse>
    </Navbar>
  );
}
