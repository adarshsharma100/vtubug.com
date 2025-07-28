
gsap.fromTo(
    ".loading-page",
    { opacity: 1 },
    {
      opacity: 0,
      display: "none",
      duration: 1,
      delay: 2.5,
    }
  );
  
  gsap.fromTo(
    ".logo-name",
    {
      y: 50,
      opacity: 0,
    },
    {
      y: 0,
      opacity: 1,
      duration: 1.5,
      delay: 0,
    }
  );
  gsap.fromTo(
    ".wrapper",
    {
      y: 50,
      opacity: 0,
    },
    {
      y: 0,
      opacity: 1,
      duration: 10,
      delay: 1.5,
    }
  );
  gsap.fromTo(
    ".char1",
    {
      y: 50,
      opacity: 0,
    },
    {
      y: 0,
      opacity: 1,
      duration: 10,
      delay: 2,
    }
  );
  gsap.fromTo(
    ".pagination",
    {
      y: 50,
      opacity: 0,
    },
    {
      y: 0,
      opacity: 1,
      duration: 10,
      delay: 2,
    }
  );